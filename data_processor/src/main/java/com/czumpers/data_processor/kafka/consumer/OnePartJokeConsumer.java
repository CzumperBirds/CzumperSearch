package com.czumpers.data_processor.kafka.consumer;

import com.czumpers.data_processor.kafka.mapper.OnePartJokeMapper;
import com.czumpers.data_processor.kafka.model.OnePartJokeConsumed;
import com.czumpers.data_processor.kafka.model.ResourceProduced;
import com.czumpers.data_processor.kafka.producer.ResourceProducer;
import com.czumpers.data_processor.mongo.service.OnePartJokeService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Slf4j
@Service
@RequiredArgsConstructor
public class OnePartJokeConsumer {

    private final OnePartJokeService onePartJokeService;
    private final OnePartJokeMapper onePartJokeMapper;
    private final ResourceProducer resourceProducer;

    @KafkaListener(
            topics = "one-part-jokes",
            groupId = "spring-middleman",
            properties = {"spring.json.value.default.type=com.czumpers.data_processor.kafka.model.OnePartJokeConsumed"}
    )
    public void consume(OnePartJokeConsumed joke) {
        if (onePartJokeService.isNewJoke(joke)) {
            log.info("#### -> New one part joke saved -> id: {}", joke.getId());
            onePartJokeService.saveJoke(joke);
            ResourceProduced resource = onePartJokeMapper.mapToResource(joke);
            resourceProducer.sendMessage(resource);
        } else {
            log.info("#### -> Duplicate one part joke -> id: {}", joke.getId());
        }
    }
}
