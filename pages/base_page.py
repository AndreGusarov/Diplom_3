import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем ссылку')
    def open_link(self, url):
        return self.driver.get(url)

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Вставить текст')
    def set_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получение текущего текста')
    def get_actual_text(self, locator):
        actual_text = self.driver.find_element(*locator).text
        return actual_text
    
    @allure.step('Проверка присутствия элемента')
    def check_presence(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    @allure.step('Проверка невидимости элемента')
    def check_element_invisibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    @allure.step('Проверка видимости элемента')
    def wait_until_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))  
        
    """@allure.step('Перетащить элемент')
    def drag_and_drop(self, first_locator, second_locator):
        draggeble = self.driver.find_element(*first_locator)
        droppable = self.driver.find_element(*second_locator)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggeble, droppable).perform()
        """
    @allure.step('Перетащить элемент с помощью JS')
    def drag_and_drop(self, first_locator, second_locator):
        source = self.driver.find_element(*first_locator)
        target = self.driver.find_element(*second_locator)
        js = """
        function createEvent(typeOfEvent) {
            var event = document.createEvent("CustomEvent");
            event.initCustomEvent(typeOfEvent, true, true, null);
            event.dataTransfer = {
                data: {},
                setData: function(key, value) {
                    this.data[key] = value;
                },
                getData: function(key) {
                    return this.data[key];
                }
            };
            return event;
        }
        function dispatchEvent(element, event, transferData) {
            if (transferData !== undefined) {
                event.dataTransfer = transferData;
            }
            if (element.dispatchEvent) {
                element.dispatchEvent(event);
            } else if (element.fireEvent) {
                element.fireEvent("on" + event.type, event);
            }
        }
        function simulateHTML5DragAndDrop(element, destination) {
            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(element, dragStartEvent);
            var dropEvent = createEvent('drop');
            dispatchEvent(destination, dropEvent, dragStartEvent.dataTransfer);
            var dragEndEvent = createEvent('dragend');
            dispatchEvent(element, dragEndEvent, dropEvent.dataTransfer);
        }
        simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(js, source, target)
    @allure.step('Перемещение и клик')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).click().perform()

    @allure.step('Дождаться пока элемен будет доступен для нажатия')
    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        
    @allure.step('Найти элементы на странице')
    def find_elements(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step('Дождаться появления текста в элементе')
    def wait_text_to_be_present_in_element(self, locator, text):
        return WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(locator, text))
        
    @allure.step('Дождаться появления всех элементов')
    def wait_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url
