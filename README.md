Branch Amelia (epiche 1-6)/
│
├── src/
│   ├── __init__.py
│   │
│   ├── controller/
│   │   ├── __init__.py
│   │   ├── action_runner.py          ← Epic 1-2 (US4)
│   │   ├── game_controller.py        ← MERGED: Epic 4 + 5 (US13, US16-17)
│   │   ├── input_manager.py          ← Epic 1-2 (US6, US7)
│   │   ├── render_controller.py      ← Epic 3 (US10, US11, US12)
│   │   ├── room_manager.py           ← Epic 1-2 (US2)
│   │   └── state_machine.py          ← Epic 1-2 (US1)
│   │
│   ├── model/
│   │   ├── __init__.py
│   │   ├── animation.py              ← Epic 3 (US12)
│   │   ├── character.py              ← Epic 4 FIXED (US14)
│   │   ├── flag_manager.py           ← Epic 1-2 (US5)
│   │   ├── game.py                   ← MERGED: Epic 4 + 5 (US13, US18)
│   │   ├── input_actions.py          ← Epic 1-2 (US6)
│   │   ├── input_context.py          ← Epic 1-2 (US7)
│   │   ├── migration.py              ← Epic 5 (US19)
│   │   ├── persistent_world_state.py ← Epic 1-2 (US5.5)
│   │   ├── render_system.py          ← Epic 3 (US10, US11)
│   │   ├── room_data.py              ← MERGED: Epic 1-2 + 3 (US2, US3, US11)
│   │   ├── script_actions.py         ← Epic 1-2 (US4)
│   │   │
│   │   ├── save/                     ← Epic 5 SPLIT (US16-19)
│   │   │   ├── __init__.py
│   │   │   ├── constants.py
│   │   │   ├── dtos.py
│   │   │   ├── manager.py
│   │   │   ├── serializer.py
│   │   │   └── validator.py
│   │   │
│   │   └── states/
│   │       ├── __init__.py
│   │       ├── base_state.py         ← Epic 1-2 (US1)
│   │       └── game_states.py        ← Epic 1-2 (US1)
│   │
│   └── view/
│       ├── __init__.py
│       ├── gameplay_menu.py          ← Epic 5
│       ├── main_menu.py              ← MERGED: Epic 4 + 5 (US13, US17)
│       ├── room_view.py              ← Epic 3 (US10, US11)
│       └── save_menu.py              ← Epic 5 (US16, US17)
│
├── tests/
│   ├── __init__.py
│   │
│   ├── controller/
│   │   ├── __init__.py
│   │   ├── test_action_runner.py     ← Epic 1-2 (US4)
│   │   ├── test_game_controller.py   ← MERGED: Epic 4 + 5 (US13, US16-17)
│   │   ├── test_input_manager.py     ← Epic 1-2 (US6)
│   │   ├── test_room_manager.py      ← Epic 1-2 (US2)
│   │   └── test_state_machine.py     ← Epic 1-2 (US1)
│   │
│   ├── model/
│   │   ├── __init__.py
│   │   ├── test_animation.py         ← Epic 3 (US12)
│   │   ├── test_camera.py            ← Epic 3 (US11)
│   │   ├── test_character.py         ← UPDATED: Epic 4 (US14)
│   │   ├── test_flag_manager.py      ← Epic 1-2 (US5)
│   │   ├── test_game.py              ← Epic 4 (US13)
│   │   ├── test_input_context.py     ← Epic 1-2 (US7)
│   │   ├── test_persistent_world.py  ← Epic 1-2 (US5.5)
│   │   ├── test_render_system.py     ← Epic 3 (US10)
│   │   ├── test_room_data.py         ← MERGED: Epic 1-2 + 3 (US3, US11)
│   │   └── test_save.py              ← MERGED: Epic 5 (US16-19)
│   │
│   └── view/
│       ├── __init__.py
│       ├── test_main_menu.py         ← MERGED: Epic 4 + 5 (US13, US17)
│       └── test_room_view.py         ← Epic 3 (US10, US11)
│
├── design_patterns/
│   ├── core_architecture/            ← Epic 1-2
│   │   ├── flags_condition.puml
│   │   ├── room_system.puml
│   │   ├── script_system.puml
│   │   └── state_machine.puml
│   │
│   ├── input_system/                 ← Epic 1-2
│   │   ├── input_context.puml
│   │   └── input_manager.puml
│   │
│   ├── presentation/                 ← Epic 3
│   │   ├── animation_system.puml
│   │   ├── camera_system.puml
│   │   └── render_pipeline.puml
│   │
│   └── save_load/                    ← Epic 5
│       ├── migration.puml
│       └── save_system.puml
│
├── saves/                            ← Runtime save directory
│   └── (slot_01.json, etc.)
│
└── README.md
