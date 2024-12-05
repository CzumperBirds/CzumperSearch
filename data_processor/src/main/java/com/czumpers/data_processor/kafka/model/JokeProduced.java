package com.czumpers.data_processor.kafka.model;

import lombok.Data;

import java.util.Map;

@Data
public class JokeProduced {
    private boolean error;
    private String category;
    private String type;
    private String setup;
    private String delivery;
    private Map<String, Boolean> flags;
    private int id;
    private boolean safe;
    private String lang;
}
