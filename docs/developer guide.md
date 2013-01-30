# Developer Guide
Feel free to contribute to catntent. Contributions are *only* accepted if
they are BSD licensed. Most of the time I would prefer it if you would
stick to PEP8, beside 80 characters per line. Just do not do it. Writing
Django models with a 80 character limit is just ugly.

Things to keep in mind

- apps do not depend on each other
- if your app should work with others use signals
- each new app, which users interact with, needs support for `dashboard`
- functionality which is not app specific goes to `common`
- if you need settings use environment variables and document them in the `README.md`
- send pull requests, I will not accept anything else
- if you are not sure if a feature is already in work open an issue
- provide a navigation fixture
