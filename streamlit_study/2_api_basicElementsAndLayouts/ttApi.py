import pandas as pd
import json

product = json.loads('''{
    "code": 0,
    "data": {
        "latest_available_date": "2024-12-03",
        "next_page_token": "",
        "products": [
            {"click_through_rate": "0.0337", "gmv": {"amount": "361.50", "currency": "USD"}, "id": 1729632228679520599, "orders": 11, "units_sold": 11},
            {"click_through_rate": "0.1781", "gmv": {"amount": "175.00", "currency": "USD"}, "id": 1729632228679651671, "orders": 23, "units_sold": 23},
            {"click_through_rate": "0.0451", "gmv": {"amount": "146.60", "currency": "USD"}, "id": 1729619467564716375, "orders": 5, "units_sold": 6},
            {"click_through_rate": "0.0249", "gmv": {"amount": "139.93", "currency": "USD"}, "id": 1729619473473966423, "orders": 5, "units_sold": 6},
            {"click_through_rate": "0.0467", "gmv": {"amount": "120.00", "currency": "USD"}, "id": 1729619477102629207, "orders": 3, "units_sold": 3},
            {"click_through_rate": "0.0349", "gmv": {"amount": "110.34", "currency": "USD"}, "id": 1729619472417984855, "orders": 5, "units_sold": 5},
            {"click_through_rate": "0.0371", "gmv": {"amount": "0.00", "currency": "USD"}, "id": 1729632223314219351, "orders": 1, "units_sold": 1},
            {"click_through_rate": "0.0505", "gmv": {"amount": "0.00", "currency": ""}, "id": 1729619475387093335, "orders": 0, "units_sold": 0},
            {"click_through_rate": "0.0265", "gmv": {"amount": "0.00", "currency": ""}, "id": 1729619539120132439, "orders": 0, "units_sold": 0}
        ],
        "total_count": 9
    },
    "message": "Success",
    "request_id": "202412041032551B5E1B08FB80AC00E1C5"
}''')
# Parse the product data into a DataFrame
product_data = product  # product는 이미 파이썬 딕셔너리입니다.
#  https://partner.us.tiktokshop.com/dev/api-testing-tool?apiId=7369112376995694352&pkgId=948484&versionId=202405
df = pd.json_normalize(product_data['data']['products'])  # Normalize the products data into a DataFrame




