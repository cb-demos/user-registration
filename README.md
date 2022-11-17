# Thunder Demo User Registration form

**Purpose**: Allow users to join the Thunder Demo environment.

## Info

* Built using [Flask](https://flask.palletsprojects.com/en/1.1.x/).

### Environment variables

| Env var | Example | Description |
| --- | --- | --- |
| LDAP_ADMIN | username | Username of a FreeIPA user who has user admin privileges. |
| LDAP_PASSWORD | password | Password of the FreeIPA user admin. |
| LDAP_SERVER | ipa.example.com | URL (don't include protocol) of your FreeIPA server. |
| INVITE_CODE | attendee2020 | Set an invite code for basic level of access to restrict who has access to signup. |
| USER_GROUP | attendee | Set the FreeIPA user group for those who sign up with INVITE_CODE value. |
| ELEVATED_INVITE_CODE | admin2020 | Set the invite code for users with elevated level of access (e.g. workshop admins). |
| ELEVATED_USER_GROUP | sa-users | Set the FreeIPA user group for those who sign up with the ELEVATED_INVITE_CODE value. |
| TARGET_URL | https://example.com/cjoc/ | URL to access the SDA instance. |

### How to run

#### Locally

```bash
# If you don't have pipenv installed, install it
pip install pipenv

# Now install the dependencies
pipenv install

# Run the application (Must have the above environment variables set)
pipenv run gunicorn app:app --bind 0.0.0.0:8000

# The service is now available on port 8000.
```

#### Docker

```
# First build the image
docker build -t user-registration .

# Now run it, filling in the parameters with appropriate values
docker run -p 8000:8000 -e LDAP_ADMIN=admin -e LDAP_PASSWORD=password \
  -e LDAP_SERVER=ipa.example.com user-registration
```

## Todo

* [x] Integrate with FreeIPA
* [x] Create Dockerfile
* [x] Add multiple invite codes for different levels
