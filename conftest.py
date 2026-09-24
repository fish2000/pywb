import pytest

@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    if config.pluginmanager.has_plugin("clu_pytest"):
        plugin = config.pluginmanager.get_plugin("clu_pytest")
        config.pluginmanager.unregister(plugin, name="clu_pytest")
    if config.pluginmanager.has_plugin("python-clu"):
        plugin = config.pluginmanager.get_plugin("python-clu")
        config.pluginmanager.unregister(plugin, name="python-clu")
    if config.pluginmanager.has_plugin("python_clu"):
        plugin = config.pluginmanager.get_plugin("python_clu")
        config.pluginmanager.unregister(plugin, name="python_clu")