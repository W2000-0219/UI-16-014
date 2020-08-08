import allure

class Test001:
    @allure.step("下单")
    def input_value(self):
        print("\ninput_value")

    @allure.step("登录")
    def test_001(self):
        self.input_value()
        print("\ntest_001")
        assert True