package com.czumpers.data_processor.kafka.model;

import lombok.Data;
import lombok.EqualsAndHashCode;

import java.util.Map;


@Data
@EqualsAndHashCode(of = {"id", "type", "category", "joke"})
public class OnePartJokeConsumed {
    private int id;
    private String type;
    private String category;
    private Map<String, Boolean> flags;
    private String joke;
}
