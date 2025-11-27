from setuptools import setup, find_packages

setup(name='SHICTHRSLogCore',
      version='1.7.0',
      description='SHICTHRS LOG CORE logging system',
      url='https://github.com/JNTMTMTM/SHICTHRS_LogCore',
      author='SHICTHRS',
      author_email='contact@shicthrs.com',
      license='GPL-3.0',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['colorama==0.4.6' , 'pytz==2025.2' , 'SHICTHRSConfigLoader==1.2.0'],
      zip_safe=False)
