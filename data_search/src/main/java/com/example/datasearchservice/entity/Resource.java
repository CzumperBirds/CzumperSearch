package com.example.datasearchservice.entity;

import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.elasticsearch.annotations.Document;

import java.io.Serial;
import java.io.Serializable;
import java.util.List;

@Getter
@Setter
@Document(indexName = "resource")
public class Resource implements Serializable {

    @Serial
    private static final long serialVersionUID = 1L;

    @Id
    private String id;
    private String type;
    private String source;
    private String content;
    private String published;
    private List<String> tags;
}
