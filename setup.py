from setuptools import setup, find_packages

setup(
    name='data-quality-tool',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
        'jinja2',
        # You can add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'data_quality_checker=data_quality_tool.data_quality_checker:main',
        ],
    },
    include_package_data=True,
)