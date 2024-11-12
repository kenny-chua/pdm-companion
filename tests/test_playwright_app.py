# import re
# from playwright.sync_api import Page, expect


# def test_has_title(page: Page):
#     page.goto("http://localhost:8501/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Streamlit"))


# def test_has_button(page: Page):
#     page.goto("http://localhost:8501/")

#     # Click the get started link.
#     page.get_by_role("link", name="Testimonials").click()
