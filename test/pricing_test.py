# test passeed
# from tools.validation import Validator
# def test_valid(test_name,validator,value):
#     try:
#         validator(value)
#     except ValueError:
#         print(f"{test_name}: Failed")
#     else:
#         print(f"{test_name}:Passed")
#
# def test_invalid(test_name,validator,value):
#     try:
#         validator(value)
#     except ValueError:
#         print(f"{test_name}:Passed")
#     else:
#         print(f"{test_name}:Failed")
#
# # Printing Price
# test_valid("Printing Price Valid",
#            Validator.printing_price_validator, 25_000_000)
#
# test_invalid("Printing Price Invalid",
#              Validator.printing_price_validator, -100)
#
# # Litho Price
# test_valid("Litho Price Valid",
#            Validator.litho_price_validator, 4_500_000)
#
# test_invalid("Litho Price Invalid",
#              Validator.litho_price_validator, 0)
#
# # Cellophane Price
# test_valid("Cellophane Price Valid",
#            Validator.cellophane_price_per_cm_validator, 100)
#
# test_invalid("Cellophane Price Invalid",
#              Validator.cellophane_price_per_cm_validator, "100")
# .............................................................................
# test passed
# from model.pricing import Pricing
#
# pricing_1 = Pricing(
#     25_000_000,
#     4_500_000,
#     100
# )
#
# print(pricing_1.printing_price)
# print(pricing_1.litho_price)
# print(pricing_1.cellophane_price_per_cm)
#
# pricing_1.cellophane_price_per_cm=-100
# print(pricing_1.cellophane_price_per_cm)