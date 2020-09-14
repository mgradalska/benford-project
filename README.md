# benford-project

Application analyzing if given dataset satisfies Benford's law or not.

## Requirements
To run application [docker-compose](https://docs.docker.com/compose/install/) is needed.

## Run application
To run application execute following comands in `benford-project` directory:
```bash
docker-compose up
```

After that application interface will be available under localhost:4200 link. 

Backend API: localhost:8000/api.

## Test application
To run backend tests execute following command (the application has to be running):
```bash
docker-compose exec web python benford_backend/manage.py test benford_analyzer
```

## Explanation

Application checks if given dataset satisfies Benford's law by 
[Chi Square](https://www.statisticshowto.com/probability-and-statistics/chi-square/) 
statistic test with 95% significance level. 

Application input:
- Flat text file with required '7_2009' column which contains only integer data

Application output:
- Information if given data satisfies Benford's law or not
- Generated graph with given data first number's frequency distribution compared to Benford's distribution