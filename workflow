name: zb

on:
  schedule:
    - cron: '0 06,20 * * *'
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2
    
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x

      - name: Install dependencies
        run: pip install selenium requests futures eventlet pypinyin
              
      - name: Run ZB
        run: python ${{ github.workspace }}/DXZB.py

      - name: 提交更改
        run: |
          git config --local user.email "vjfchen@sina.com"
          git config --local user.name "mlzlzj"
          git add .
          git commit *.txt -m "Add generated file"
          git commit *.m3u -m "Add generated file"
          #git pull --rebase
          git push -f
