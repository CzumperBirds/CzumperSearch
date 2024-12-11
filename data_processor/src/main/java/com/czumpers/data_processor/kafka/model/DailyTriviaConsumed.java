package com.czumpers.data_processor.kafka.model;

import lombok.Data;
import lombok.EqualsAndHashCode;

import java.util.List;
import java.util.Map;

@Data
public class DailyTriviaConsumed {
    private String id;
    private String title;
    private String link;
    private String author;
    private String published;
    private List<Map<String, String>> tags;
}
