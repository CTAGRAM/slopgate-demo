# pagekit

Tiny, dependency-free pagination helpers for Python.

```python
from pagekit import page, page_count

page_count(total=95, size=10)    # 10
page(list(range(95)), 2, 10)     # [10, 11, ..., 19]
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Run the tests with `python -m pytest`.

*This repository is the live demo playground for [SlopGate](https://github.com/CTAGRAM/slopgate).*
