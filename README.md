# Trustwise Assignment

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/yash2002vardhan/trustwise-assignment.git
cd trustwise-assignment
```

2. Start the application
```bash
docker compose up --build -d
```

The application will be built and started in detached mode. You can check the logs using:
```bash
docker compose logs -f
```

To stop the application:
```bash
docker compose down
```

## Environment Variables

Make sure to set up your environment variables in a `.env` file before running the application. You can copy the example file:
```bash
cp .env.example .env
```

Then edit the `.env` file with your actual configuration values.
