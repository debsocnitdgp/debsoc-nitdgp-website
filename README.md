<p align="center">
  <a href="http://debsocnitd.herokuapp.com">
    <img alt="logo" src="sitewebapp/static/debsoclogo.png" width="100" />
  </a>
</p>
<h1 align="center">
  The Debating Society, Nit Durgapur
</h1>

<p align="center">
<a href="https://github.com/rishav4101/debsocnitdWeb/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/rishav4101/debsocnitdWeb"></a>
<a href="https://github.com/rishav4101/debsocnitdWeb/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/rishav4101/debsocnitdWeb"></a>
<a href="https://github.com/rishav4101/debsocnitdWeb/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/rishav4101/debsocnitdWeb"></a>
<a href="https://github.com/rishav4101/debsocnitdWeb/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/rishav4101/debsocnitdWeb"></a>
</p>

## Description

The official website of Debating Society, Nit Durgapur. Built with [Django](https://www.djangoproject.com/) and [MDB](https://mdbootstrap.com/).

## Project status

Live. Visit at [http://www.debsocnitdgp.in](http://www.debsocnitdgp.in).

## Application is dockerized

## Installation and usage

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install virtual environment outside the root directory.

- Clone the repository.
- Create a new virtual env with [pip](https://pip.pypa.io/en/stable/).
- cd to project directory (eg : cd debsocnitdWeb/).
- Install requirements.

```bash
python install -r requirements.txt
```

- Make migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

- Create superuser to access and manage database, and enter the details asked.

```bash
python manage.py createsuperuser
```

- Run Project on local server.

```bash
python manage.py runserver
```

- Congratulations! You have finally built the project. Now head over to the localhost your browser to access the Website.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change, and please provide a good description of the issue.

## License

[MIT](./LICENSE)
