package com.czumpers.data_processor.kafka.model;

import lombok.Data;
import lombok.EqualsAndHashCode;

import java.util.Map;

@Data
@EqualsAndHashCode(of = {"id", "type", "category", "setup", "delivery"})
public class TwoPartJokeConsumed {
    private int id;
    private String type;
    private String category;
    private Map<String, Boolean> flags;
    private String setup;
    private String delivery;
}