package com.czumpers.data_processor.kafka.producer;

import com.czumpers.data_processor.kafka.model.ResourceProduced;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Slf4j
@Service
@RequiredArgsConstructor
public class ResourceProducer {

    private static final String TOPIC = "processed-resources";
    private final KafkaTemplate<String, ResourceProduced> kafkaTemplate;

    public void sendMessage(ResourceProduced resource) {
        kafkaTemplate.send(TOPIC, resource);
    }
}
