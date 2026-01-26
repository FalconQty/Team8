# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# --- CONFIGURAZIONE ---
APP_NAME = 'Sikula'
SHOW_TERMINAL = False  # Metti True se vuoi vedere i log di errore, False per release finale
# ----------------------

a = Analysis(
    ['src/app.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('data', 'data'),
        ('assets', 'assets'),
        # Nota: logs e saves vengono creati a runtime, 
        # non è strettamente necessario includerli qui se sono vuoti, 
        # ma lasciarli non fa danni.
        ('logs', 'logs'),
        ('saves', 'saves'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=SHOW_TERMINAL, 
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='assets/icon.icns' # <--- SCOMMENTA SE HAI L'ICONA (Mac usa .icns, Win usa .ico)
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=APP_NAME, # Ora la cartella si chiamerà 'Sikula'
)