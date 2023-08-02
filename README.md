## **Safety-Bridge-Design v0.1.3**
### 【剪力、彎矩、撓度】可視化與動態可視化
+ **Version: Python 3.10.9**

![alt](https://raw.githubusercontent.com/RogelioKG/Safety-Bridge-Design/main/animation.gif)

> ### **`Execute`**
> 
> 在 Safety-Bridge-Design 目錄下執行 CMD，輸入： 
> ```
> py tests_entry.py
> ```
> 接著輸入想測試的檔案名稱
> ```
> test file name: 檔案名稱(需放置於 tests 目錄)
> ```

> ### **`Patch Notes`**
> + #### **v0.1.1**
> 1. ...
>
> + #### **v0.1.2**
> 1. Beam、Loading、Support 使用物件導向設計
> 2. 更改檔案架構，並以 tests_entry 做為執行入口 
>
> + #### **v0.1.3**
> 1. 函式名稱改為 PEP8 命名
> 2. test_API (統一讓使用者直接調用 draw 函式繪圖)
> 3. staticmethod Loading.splitter\
> (區段 distributed loading 不再需使用者預先計算出等效的分離 loadings，現可交由該函式計算)
