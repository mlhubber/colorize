#!/bin/sh

model_url="https://github.com/foamliu/Simple-Colorization/releases/download/v1.0/model.06-2.5489.hdf5"
model_name=${model_url##*/}
dependencies="numpy tensorflow keras opencv pydot graphviz"

######################################################################
# Setup

# Call mlhub.utils.create_package_cache_dir to get the package-specific cache dir.
# Then link it into ./cache

cache_dir="$(python -c "from mlhub import utils; print(utils.create_package_cache_dir())")"
ln -s ${cache_dir} cache
cache_dir="cache"

# Change dir to ./cache to make following work inside ./cache

cd ${cache_dir}

######################################################################
# Download pre-built model.
#
# **Note**: images are packaged instead of downloaded.

dr="models"
if [[ ! -d ${dr} ]]; then
  mkdir ${dr}
fi

pushd ${dr} 1>/dev/null

if [[ ! -f ${dr}/${model_name} ]]; then
  echo "Downloading the pre-built model itself (95M) which can take a minute or two..."
  wget ${model_url}
  echo ""
fi

popd 1>/dev/null

######################################################################
# Install dependencies

echo "Installing dependencies:" ${dependencies}

# Check uninstalled dependencies

installed="$(conda list)"
uninstalled=''
for pkg in ${dependencies}; do
  if [[ -z $(echo "${installed}" | grep -E "^${pkg} ") ]]; then
    uninstalled="${pkg} ${uninstalled}"
  fi
done

# Install uninstalled dependencies

if [[ ! -z ${uninstalled} ]]; then
  conda install "$uninstalled"
fi
