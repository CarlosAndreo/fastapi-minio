<div align="center">

# FastAPI MinIO <!-- omit in toc -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

[![fastapi-minio][fastapi-minio-badge]][fastapi-minio-url]

[Wiki](https://github.com/CarlosAndreo/fastapi-minio/wiki)

</div>

## :brain: About

This is a ready-to-use project template for building FastAPI applications with MinIO. It's designed to help you get started quickly with a clean architecture, pre-configured settings, and best practices for scalability and maintainability.

## :hammer_and_wrench: Stack
- [![Python][python-badge]][python-url] - Programming language.
- [![FastAPI][fastapi-badge]][fastapi-url] - Python framework for web applications to expose the API.
- [![MinIO][minio-badge]][minio-url] - Bucket to store data.

## :rocket: Getting Started Locally

Install Docker following the instructions for your operating system:

- [Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

- [Ubuntu](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

- [MacOS](https://docs.docker.com/desktop/install/mac-install/)

Clone the repository:

```bash
git clone https://github.com/CarlosAndreo/fastapi-minio.git
cd fastapi-minio
```

Build the Docker image:

```bash
docker compose build
```

Run the Docker container:

```bash
docker compose up -d
```

The application will be available at `http://localhost:8000`.

The MinIO UI will be available at `http://localhost:9000`.

## Contributors <!-- omit in toc -->

<a href="https://github.com/CarlosAndreo/fastapi-minio/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=CarlosAndreo/fastapi-minio" />
</a>

[fastapi-minio-badge]: https://img.shields.io/github/v/release/CarlosAndreo/fastapi-minio?label=fastapi-minio&color=blue
[fastapi-minio-url]: https://github.com/CarlosAndreo/fastapi-minio/releases/latest
[contributors-shield]: https://img.shields.io/github/contributors/CarlosAndreo/fastapi-minio.svg?style=for-the-badge
[contributors-url]: https://github.com/CarlosAndreo/fastapi-minio/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/CarlosAndreo/fastapi-minio.svg?style=for-the-badge
[forks-url]: https://github.com/CarlosAndreo/fastapi-minio/network/members
[stars-shield]: https://img.shields.io/github/stars/CarlosAndreo/fastapi-minio.svg?style=for-the-badge
[stars-url]: https://github.com/CarlosAndreo/fastapi-minio/stargazers
[issues-shield]: https://img.shields.io/github/issues/CarlosAndreo/fastapi-minio.svg?style=for-the-badge
[issues-url]: https://github.com/CarlosAndreo/fastapi-minio/issues
[license-shield]: https://img.shields.io/github/license/CarlosAndreo/fastapi-minio.svg?style=for-the-badge
[license-url]: https://github.com/CarlosAndreo/fastapi-minio/blob/main/LICENSE
[python-badge]: https://img.shields.io/badge/Python-3.13.3-blue?style=for-the-badge&logo=python&logoColor=white&labelColor=3776AB
[python-url]: https://www.python.org/downloads/release/python-3133/
[fastapi-badge]: https://img.shields.io/badge/FastAPI-0.115.12-blue?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=009688
[fastapi-url]: https://fastapi.tiangolo.com/
[minio-badge]: https://img.shields.io/badge/MinIO-RELEASE.2025--04--22--T22--12--26Z-ff2364?style=for-the-badge&logo=minio&logoColor=white&labelColor=ff2364
[minio-url]: https://min.io/
