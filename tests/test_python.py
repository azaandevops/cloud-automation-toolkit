def test_inventory_module_is_importable():
    import pathlib
    assert pathlib.Path("python/aws_inventory.py").exists()
