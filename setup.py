from setuptools import setup

setup(
  name='ai-safety-gridworlds-viewer',
    version='0.1',
    description='An agent viewer for ai-safety-gridworlds',
    long_description = (
      'This project is created to enable display of a live game as an' 
      '"agent" plays it. This is desirable in reinforcement learning (RL)'
      'settings, where one need to view interactions of an agent with the'
      'environment as the game progresses.'), 

    url='http://github.com/n0p2/ai-safety-gridworlds-viewer',
    author='n0p2',
    author_email='N/A',
    license='Apache 2.0',
    packages=['ai_safety_gridworlds_viewer'],

    install_requires=[
      'enum34',  # required by ai-safety-gridworlds 
      'abseil-py', 
      'ai-safety-gridworlds' 
    ],

    dependency_links=[
      'https://github.com/abseil/abseil-py/tarball/master#egg=abseil-py-0.1.7', # required by ai-safety-gridworlds 
      'https://github.com/deepmind/ai-safety-gridworlds/tarball/master#egg=ai-safety-gridworlds-0.1'
    ],

    classifiers=[
      'Environment :: Console',
      'Environment :: Console :: Curses',
      'Intended Audience :: Education',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: Apache Software License',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX',
      'Operating System :: Unix',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.6',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Software Development :: Libraries',
    ],

    keywords=(
      'ai '
      'gridworld '
      'reinforcement learning '
    ),
    zip_safe=True
)
