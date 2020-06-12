from src.sample import Sample


def test_sample_add():
    # Sample.add は空の実装なので、その修正しない限りこのテストは失敗します！
    assert Sample().add(3, 4) == 7
