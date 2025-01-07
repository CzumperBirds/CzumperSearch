FROM grafana/grafana:latest

# Switch to root user to install packages
USER root

# Install jq and curl using apk (Alpine package manager)
RUN apk add --no-cache jq curl

# Switch back to grafana user
USER grafana

#[Entrypoint]
