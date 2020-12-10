FROM cmusei/st2packs:builder-3.3dev AS builder

# Install custom packs
RUN /opt/stackstorm/st2/bin/st2-pack-install ${PACKS}

COPY actions /opt/stackstorm/packs/vsphere/actions

###########################
# Minimize the image size. Start with alpine:3.8,
# and add only packs and virtualenvs from builder.
FROM stackstorm/st2packs:runtime

VOLUME ["/opt/stackstorm/packs", "/opt/stackstorm/virtualenvs"]

# Copy packs and virtualenvs
COPY --from=builder /opt/stackstorm/packs /opt/stackstorm/packs
COPY --from=builder /opt/stackstorm/virtualenvs /opt/stackstorm/virtualenvs