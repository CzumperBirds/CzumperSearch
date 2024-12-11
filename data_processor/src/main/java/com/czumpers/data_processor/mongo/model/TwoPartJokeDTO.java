package com.czumpers.data_processor.mongo.model;

import lombok.AllArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@AllArgsConstructor
@Document(collection = "two_part_jokes")
public class TwoPartJokeDTO {
    @Id
    private int jokeId;
}
