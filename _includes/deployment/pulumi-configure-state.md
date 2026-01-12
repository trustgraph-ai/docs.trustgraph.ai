You need to tell Pulumi which state to use. You can store this in an S3
bucket, but for experimentation, you can just use local state:

```sh
pulumi login --local
```

When storing secrets in the Pulumi state, pulumi uses a secret passphrase
to encrypt secrets. When using Pulumi in a production or shared
environment you would have to evaluate the security arrangements around
secrets.

We're just going to set this to the empty string, assuming that no
encryption is fine for a development deploy.

```sh
export PULUMI_CONFIG_PASSPHRASE=
```
