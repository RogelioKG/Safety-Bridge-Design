# Safety-Bridge-Design
<!-- Badges -->
![Version: 1.1.0](https://img.shields.io/badge/version-1.1.0-blue)
[![Python: 3.10.9](https://img.shields.io/badge/python-3.10.9-blue)](https://www.python.org/downloads/release/python-3109/ "More details about Python 3.10.9")
![Last Update: 2023/7/31](https://img.shields.io/badge/last%20update-2023/7/31-darkgreen)
[![Licence: MIT](https://img.shields.io/github/license/RogelioKG/Safety-Bridge-Design)](./LICENSE)

## Brief
【剪力、彎矩、撓度】可視化與動態可視化
<!-- GIF -->
![animation](./animation.gif)

## Run Script
```
py tests_entry.py
```
接著輸入想測試的檔案名稱即可。
> [!IMPORTANT]
> 該檔案需在 `tests` 目錄下。

## Patch Notes
+ v0.1.1
  1. ...

+ v0.1.2
  1. Beam, Loading, Support 使用 OOP
  2. 更改檔案架構，並以 tests_entry 做為執行入口 

+ v0.1.3
  1. 函式名稱改為 PEP8 命名
  2. test_API (統一讓使用者直接調用 draw 函式繪圖)
  3. `staticmethod Loading.splitter` (區段 distributed loading 不再需使用者預先計算出等效的分離 loadings，現可交由該函式計算)
