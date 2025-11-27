import setuptools

setuptools.setup(
      version='0.1.0',
      description='Code for reproducing the results of Neural Symbolic Regression that scales',
      name="nesymres",
      packages=setuptools.find_packages('.'),
      package_dir={'': '.'},
      install_requires=[
          'numpy==1.22.4',
          'sympy==1.13.3',
          'pandas==1.3.5',
          'click==8.1.8',
          'tqdm==4.67.1',
          'numexpr==2.8.6',
          'jsons==1.6.3',
          "h5py==3.11.0",
          "scipy==1.7.3",
          "dataclass_dict_convert==1.7.4",
          "hydra-core==1.0.0",
          "ordered_set==4.1.0",
          "wandb==0.23.0",
          "pytorch_lightning==1.8.5",
          "omegaconf==2.1.2"
      ]
     )
