package com.example.datasearchservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

@SpringBootApplication
@EnableCaching
public class DataSearchServiceApplication {

    public static void main(String[] args) {
        SpringApplication.run(DataSearchServiceApplication.class, args);
    }

}
