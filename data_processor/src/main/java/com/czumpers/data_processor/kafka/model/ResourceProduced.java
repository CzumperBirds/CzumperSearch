package com.czumpers.data_processor.kafka.model;

import lombok.Data;

import java.util.List;

@Data
public class ResourceProduced {
    private String type;
    private String source;
    private String content;
    private String published;
    private List<String> tags;
}
