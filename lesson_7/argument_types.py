from typing import List


from typing import List


def get_common_balance(user_id: str, balances: List[int]) -> dict:
    result = 0

    for balance in balances:
        result += balance

    return result


# print(get_common_balance("12345", [10, 20, 30]))  # correct
# print(get_common_balance([10, 20, 30], "12345"))  # error

# print(get_common_balance(balances=[10, 20, 30], user_id="12345"))
