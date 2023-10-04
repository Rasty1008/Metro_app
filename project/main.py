from sqlalchemy.orm import Session

from fastapi import FastAPI

import models, scraper_metro
from servises import engine, SessionLocal

with Session(engine) as session:

    Rayymbek = models.Schedule(stations = scraper_metro.stations[0], rayymbek_momyshuly = scraper_metro.time_rayymbek_momyshuly[0],
                           momyshuly_rayymbek = scraper_metro.time_momyshuly_rayymbek[0])
    
    Zhibek_zholy = models.Schedule(stations = scraper_metro.stations[1], rayymbek_momyshuly = scraper_metro.time_rayymbek_momyshuly[1],
                           momyshuly_rayymbek = scraper_metro.time_momyshuly_rayymbek[1])
    
    Almaly = models.Schedule(stations = scraper_metro.stations[2], rayymbek_momyshuly = scraper_metro.time_rayymbek_momyshuly[2],
                           momyshuly_rayymbek = scraper_metro.time_momyshuly_rayymbek[2])
    
    Abaya = models.Schedule(stations = scraper_metro.stations[3], rayymbek_momyshuly = scraper_metro.time_rayymbek_momyshuly[3],
                           momyshuly_rayymbek = scraper_metro.time_momyshuly_rayymbek[3])
    
    Baikonir = models.Schedule(stations = scraper_metro.stations[4], rayymbek_momyshuly = scraper_metro.time_rayymbek_momyshuly[4],
                           momyshuly_rayymbek = scraper_metro.time_momyshuly_rayymbek[4])
    
    Theater_named_after_Mukhtar_Auezov = models.Schedule(stations = scraper_metro.stations[5], rayymbek_momyshuly = scraper_metro.time_rayymbek_momyshuly[5],
                           momyshuly_rayymbek = scraper_metro.time_momyshuly_rayymbek[5])
    
    Alatau = models.Schedule(stations = scraper_metro.stations[6], rayymbek_momyshuly = scraper_metro.time_rayymbek_momyshuly[6],
                           momyshuly_rayymbek = scraper_metro.time_momyshuly_rayymbek[6])
    
    Sairan = models.Schedule(stations = scraper_metro.stations[7], rayymbek_momyshuly = scraper_metro.time_rayymbek_momyshuly[7],
                           momyshuly_rayymbek = scraper_metro.time_momyshuly_rayymbek[7])
    
    Moscow = models.Schedule(stations = scraper_metro.stations[8], rayymbek_momyshuly = scraper_metro.time_rayymbek_momyshuly[8],
                           momyshuly_rayymbek = scraper_metro.time_momyshuly_rayymbek[8])
    
    Saryarka = models.Schedule(stations = scraper_metro.stations[9], rayymbek_momyshuly = scraper_metro.time_rayymbek_momyshuly[9],
                           momyshuly_rayymbek = scraper_metro.time_momyshuly_rayymbek[9])
    
    Momyshuly = models.Schedule(stations = scraper_metro.stations[10], rayymbek_momyshuly = scraper_metro.time_rayymbek_momyshuly[10],
                           momyshuly_rayymbek = scraper_metro.time_momyshuly_rayymbek[10])

session.add_all([Rayymbek, Zhibek_zholy, Almaly, Abaya, Baikonir, Theater_named_after_Mukhtar_Auezov,
            Alatau, Sairan, Moscow, Saryarka, Momyshuly])
session.commit()


models.Base.metadata.create_all(bind=engine)

app = FastAPI()