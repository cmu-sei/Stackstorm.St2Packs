## Reason

Originally derived from:  https://github.com/StackStorm/st2packs-dockerfiles

This Repo is made to support the Stackstorm HA configuration in K8S.  In order to properly use, you must bake in any packs you want to use into a custom docker image. 

This repo handles that by creating a pack that bakes the vsphere pack into a packs image.

It also implements 3 custom-created tasks:

- get_vms_with_uuid
- guest_process_run_fast
- guest_file_upload_content

## Command

To rebuild this image (for instance, if you need a new vsphere pack version), run the following command.  It is currently configured to build while on SEI VPN using:

```
docker build --build-arg PACKS="vsphere=1.1.0" -t cmusei/st2packs:<TAG> st2packs-image
```

All that needs to be done is to update the `<TAG>` to whatever docker image tag you want to use -- in this case, the version of the vsphere plugin is recommended.

## Push to Dockerhub

Once built, ensure this image is pushed to the `cmusei` organization in Dockerhub.

# Builder

Because of Python version dependency issues in the 3.3dev version of Stackstorm, this repo rebuilds the "builder" version of the `st2packs` image using version `3.1.0`.  If you wish to change this version in the future, edit the `st2packs-builder` Dockerfile and change the version, and then run the following commands to update the `st2packs` image in Docker Hub:

```
docker build -t cmusei/st2packs:builder st2packs-builder
```
Once built, ensure this image is pushed to the `cmusei` organization in Dockerhub.


