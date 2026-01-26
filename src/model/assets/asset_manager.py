"""
FILE: ./src/model/assets/asset_manager.py
Asset Manager - Centralized handling for graphic resources.
Updated: Added color for player2.
"""
import os
import pygame
import logging

logger = logging.getLogger(__name__)

class AssetManager:
    def __init__(self, asset_dir_name: str = "assets"):
        current_file_path = os.path.abspath(__file__)
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_file_path))))
        
        self.asset_dir = os.path.join(project_root, asset_dir_name)
        self.images: dict[str, pygame.Surface] = {}
        self.fonts: dict[str, pygame.font.Font] = {}
        
        self.color_map = {
            "player": (0, 255, 0),    # Verde (Turiddu/P1)
            "player2": (0, 255, 255), # Ciano (Rosalia/P2) <--- NUOVO
            "npc": (0, 0, 255),
            "enemy": (255, 0, 0),
            "item": (255, 255, 0),
            "prop": (150, 150, 150),
            "gate": (0, 255, 255),
            "wall": (50, 50, 50),
            "background": (20, 20, 30)
        }
        
        logger.info(f"AssetManager initialized. Looking for assets in: {self.asset_dir}")

    def get_image(
        self,
        key: str,
        width: int = 32,
        height: int = 32,
        fallback_type: str = "prop",
        preserve_aspect: bool = False
    ) -> pygame.Surface:
        cache_key = f"{key}_{width}x{height}_{'AR' if preserve_aspect else 'STRETCH'}"
        
        if cache_key in self.images:
            return self.images[cache_key]

        potential_paths = [
            os.path.join(self.asset_dir, "images", key),
            os.path.join(self.asset_dir, key)
        ]

        for path in potential_paths:
            for ext in [".png", ".jpg", ".jpeg"]:
                full_path = path if path.endswith(ext) else path + ext
                
                if os.path.exists(full_path):
                    try:
                        surf = pygame.image.load(full_path).convert_alpha()
                        if surf.get_width() != width or surf.get_height() != height:
                            if preserve_aspect:
                                iw, ih = surf.get_size()
                                if iw > 0 and ih > 0:
                                    s = min(width / iw, height / ih)
                                    new_size = (max(1, int(iw * s)), max(1, int(ih * s)))
                                    surf = pygame.transform.smoothscale(surf, new_size)
                            else:
                                surf = pygame.transform.smoothscale(surf, (width, height))
                        
                        self.images[cache_key] = surf
                        return surf
                    except Exception as e:
                        logger.warning(f"Error loading image at {full_path}: {e}")

        # Fallback se l'immagine non viene trovata
        # logger.warning(f"Asset not found: {key} in {self.asset_dir}. Using placeholder.")
        return self._create_placeholder(cache_key, width, height, fallback_type)

    def _create_placeholder(self, cache_key: str, w: int, h: int, entity_type: str) -> pygame.Surface:
        surf = pygame.Surface((w, h))
        color = self.color_map.get(entity_type, (255, 0, 255))
        surf.fill(color)
        pygame.draw.rect(surf, (255, 255, 255), surf.get_rect(), 1)
        self.images[cache_key] = surf
        return surf

    def get_font(self, size: int = 24) -> pygame.font.Font:
        key = f"default_{size}"
        if key not in self.fonts:
            self.fonts[key] = pygame.font.SysFont("Arial", size, bold=True)
        return self.fonts[key]