package com.czumpers.data_processor.kafka.consumer;

import com.czumpers.data_processor.kafka.mapper.TwoPartJokeMapper;
import com.czumpers.data_processor.kafka.model.ResourceProduced;
import com.czumpers.data_processor.kafka.model.TwoPartJokeConsumed;
import com.czumpers.data_processor.kafka.producer.ResourceProducer;
import com.czumpers.data_processor.mongo.service.TwoPartJokeService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Slf4j
@Service
@RequiredArgsConstructor
public class TwoPartJokeConsumer {

    private final TwoPartJokeService twoPartJokeService;
    private final TwoPartJokeMapper twoPartJokeMapper;
    private final ResourceProducer resourceProducer;

    @KafkaListener(
            topics = "two-part-jokes",
            groupId = "spring-middleman",
            properties = {"spring.json.value.default.type=com.czumpers.data_processor.kafka.model.TwoPartJokeConsumed"}
    )
    public void consume(TwoPartJokeConsumed joke) {
        if (twoPartJokeService.isNewJoke(joke)) {
            log.info("#### -> New two part joke saved -> id: {}", joke.getId());
            twoPartJokeService.saveJoke(joke);
            ResourceProduced resource = twoPartJokeMapper.mapToResource(joke);
            resourceProducer.sendMessage(resource);
        } else {
            log.info("#### -> Duplicate two part joke -> id: {}", joke.getId());
        }
    }
}