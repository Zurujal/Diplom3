# Diplom3

Сделано только в Chrome, тк ваш ресурс не работает с Firefox.
Для начала почините свой ресурс, либо расскажите как побеждать баги вашего ресурса, на текущий момент QA-FAIL.
Невидимые оверлеи - то обходятся, то нет. Никаких сил и нервов уже не хватает на это. Ресурс ведет себя нестабильно.
Даже в хроме прокидываются эти невидимые оверлеи.
Код для того чтобы запуск осуществлялся и в Chrome и в Firefox, но в Firefox все упадет 100%:
@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == "chrome":
        service = (webdriver.chrome.service.Service())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        options.add_argument("--window_size=1920,1080")
    else:
        service = webdriver.FirefoxService()
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
        options.add_argument("--window_size=1920,1080")
    yield driver
    driver.quit()
Локатор для вашего невидимого оверлея:
INVISIBLE_LAYOUT = By.XPATH, '//*[@class = "Modal_modal_overlay__x2ZCr"]'