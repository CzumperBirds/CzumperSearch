package com.czumpers.data_processor.kafka.model;

import lombok.Data;

import java.util.Map;


@Data
public class OnePartJokeConsumed {
    private int id;
    private String type;
    private String category;
    private Map<String, Boolean> flags;
    private String joke;
}
