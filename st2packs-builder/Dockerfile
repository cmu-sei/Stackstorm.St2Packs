FROM stackstorm/st2:3.1.0

ONBUILD ARG PACKS
ONBUILD RUN : "${PACKS:?Please add '--build-arg PACKS=\"<space separated list of pack names>\"'.}"
