package com.czumpers.data_processor.kafka.consumer;

import com.czumpers.data_processor.kafka.model.JokeProduced;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Slf4j
@Service
public class Consumer {

        @KafkaListener(topics = "jokes", groupId = "spring-middleman")
        public void consume(JokeProduced joke) {
            log.info("#### -> Consumed message -> {}", joke);
        }
}
