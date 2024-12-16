package com.example.datasearchservice.entity;

import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.elasticsearch.annotations.Document;
@Getter
@Setter
@Document(indexName = "employee")
public class Employee {
    @Id
    private String id;
    private String firstName;
    private String lastName;
    private String department;
}
