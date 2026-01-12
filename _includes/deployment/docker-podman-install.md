For Windows / MacOS it is recommended to use Docker.  For Linux, Podman is
natively available with all major distributions.  You will need to have this
installed before running this installation.

- [Install Docker Engine](https://docs.docker.com/engine/install/)
- [Install Podman Machine](http://podman.io/)

{: .note }
If you are using Docker desktop, you may need to review the resource settings
as described in this section.

<details>

<summary>Resource settings for Docker desktop</summary>

<div>
Note that if you are using Docker desktop, there are CPU and memory limits
which can be applied to limit the resources set aside for containers.
If you find that containers get stuck unresourced, you will need to allocate
more resources.  We run with 12GB of RAM and 8 CPUs allocated to TrustGraph.
These settings are on the *Settings* tab under *Resources*.
</div>

<img src="docker-desktop-resources.png" alt="Docker desktop settings screenshot"/>

</details>
