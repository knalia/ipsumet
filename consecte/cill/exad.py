def scroll(driver, px_down=100):
    """
    Scrolls the page down by the specified number of pixels.

    Args:
        driver: The WebDriver instance.
        px_down: The number of pixels to scroll down.
    """
    driver.execute_script("window.scrollBy(0, {});".format(px_down))

