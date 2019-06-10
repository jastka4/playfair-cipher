from distutils.core import setup
setup(
  name = 'PlayfairCipher',         # How you named your package folder (MyLib)
  packages = ['PlayfairCipher'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Playfair cipher package',   # Give a short description about your library
  author = 'Justyna Skalska',                   # Type in your name
  author_email = 'jastka4@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/jastka4/playfair-cipher',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/jastka4/playfair-cipher/archive/v_01.tar.gz',    # I'll explain this later on
  keywords = ['playfair', 'cipher', 'pwr'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   # Again, pick a license

    'Programming Language :: Python :: 2',      #Specify which pyhton versions that you want to support
  ],
)