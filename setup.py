from distutils.core import setup
version = '1.0.2'

setup(
  name = 'personalcapital',
  packages = ['personalcapital'], # this must be the same as the name above
  version = version,
  description = 'Personal Capital library for accessing its API',
  author = 'Haochi Chen',
  author_email = 'pypi@ihaochi.com',
  url = 'https://github.com/haochi/personalcapital',
  download_url = 'https://github.com/haochi/personalcapital/tarball/{0}'.format(version),
  keywords = ['personal capital', 'financial', 'money'],
  classifiers = [],
  install_requires=[
    "cloudscraper==1.2.58",
  ],
)
