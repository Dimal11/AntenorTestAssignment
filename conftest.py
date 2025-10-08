import pytest
import allure
from pathlib import Path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            results_dir = Path("allure-results")
            results_dir.mkdir(exist_ok=True)

            screenshot_path = results_dir / f"{item.name}.png"
            page.screenshot(path=screenshot_path)
            allure.attach.file(
                str(screenshot_path),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            trace_path = results_dir / f"{item.name}-trace.zip"
            page.context.tracing.stop(path=trace_path)
            allure.attach.file(
                str(trace_path),
                name="trace",
                attachment_type=allure.attachment_type.ZIP
            )
