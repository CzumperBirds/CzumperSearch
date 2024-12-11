package com.czumpers.data_processor.mongo.model;

import lombok.AllArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@AllArgsConstructor
@Document(collection = "daily_trivia")
public class DailyTriviaDTO {
    @Id
    private String dailyTriviaId;
}
