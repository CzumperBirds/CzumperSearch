package com.example.datasearchservice.configuration;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;

//@Configuration
public class RedisConnectionConfig {
//
//    @Value("${SPRING_REDIS_HOST:localhost}")
//    private String redisHost;
//
//    @Value("${SPRING_REDIS_PORT:6379}")
//    private int redisPort;
//
//    @Bean
//    public RedisConnectionFactory redisConnectionFactory() {
//        return new LettuceConnectionFactory(redisHost, redisPort);
//    }
//    @Bean
//    public RedisTemplate<?, ?> redisTemplate(RedisConnectionFactory connectionFactory) {
//        RedisTemplate<?, ?> template = new RedisTemplate<>();
//        template.setConnectionFactory(connectionFactory);
//
//        return template;
//    }
}

